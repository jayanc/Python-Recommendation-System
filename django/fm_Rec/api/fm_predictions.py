import pickle
import random
import pandas as pd
import scipy.sparse as sparse
import numpy as np
from scipy.sparse.linalg import spsolve
from sklearn.metrics.pairwise import cosine_similarity

grouped_purchased = pd.read_csv('cvs_data_file/online-retail.csv', header=0)

customers = list(np.sort(grouped_purchased.CustomerID.unique()))
products = list(grouped_purchased.StockCode.unique())
quantity = list(grouped_purchased.Quantity)

rows = grouped_purchased.CustomerID.astype(
    'category', categories=customers).cat.codes
cols = grouped_purchased.StockCode.astype(
    'category', categories=products).cat.codes
purchases_sparse = sparse.csr_matrix(
    (quantity, (rows, cols)), shape=(len(customers), len(products)))


def make_train(ratings, pct_test=0.2):
    test_set = ratings.copy()
    test_set[test_set != 0] = 1
    training_set = ratings.copy()
    nonzero_inds = training_set.nonzero()
    nonzero_pairs = list(zip(nonzero_inds[0], nonzero_inds[1]))
    random.seed(0)
    num_samples = int(np.ceil(pct_test*len(nonzero_pairs)))
    samples = random.sample(nonzero_pairs, num_samples)
    user_inds = [index[0] for index in samples]
    item_inds = [index[1] for index in samples]
    training_set[user_inds, item_inds] = 0
    training_set.eliminate_zeros()
    return training_set, test_set, list(set(user_inds))


product_train, product_test, product_users_altered = make_train(
    purchases_sparse, pct_test=0.2)

item_lookup = pd.read_csv('cvs_data_file/item_lookup.csv', header=0)


with open('saved_model', 'rb') as f:
    saved_model = pickle.load(f)
    model = saved_model['model']


def display_recommended_items(model, data, user_ids):
    customers_arr = np.array(customers)
    products_arr = np.array(products)
    print("customers_arr", customers_arr)
    user_id = np.where(customers_arr == user_ids)[0][0]
    print(user_ids, user_id)

    n_users, n_items = data.shape
    known_positives = item_lookup['Description'][data.tocsr()[user_id].indices]
    known_positives_df = pd.DataFrame(data=known_positives)
    print(known_positives_df, '\n', '######################################')

    scores = model.predict(user_id, np.arange(n_items))

    top_items = item_lookup['Description'][np.argsort(-scores)]
    print(top_items)


# item TO item recommendation
def display_item_to_items_recommendations(model, item_id):

    products_arr = np.array(products)

    print("products_arr", products_arr, str(item_id))
    item_id = np.where(products_arr == str(item_id))[0][0]
    print(item_id)

    return item_lookup['Description'][cosine_similarity(
        model.item_embeddings)[item_id].argsort()][-5:][::-1]
