import json
from flaskapp.models import Item


def test_get_categories(client):
    result = client.get('/get_categories')
    json_result = json.loads(result.data)

    assert len(json_result['categories']) == 1
    assert json_result['categories'][0]['category_name'] == "Phones"


def test_get_items(client):
    result = client.get('/get_items/2')
    json_result = json.loads(result.data)

    assert len(json_result['items']) == 1
    assert json_result['items'][0]['item_name'] == "iPhone 13"


def test_insert_item(client, session):
    data = {
        'category_id': 2,
        'item_name': "Samsung Galaxy S21"
    }

    result = client.post(
        '/insert_item',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )

    json_result = json.loads(result.data)

    assert json_result['status'] is True
    assert session.query(Item).filter_by(item_name="Samsung Galaxy S21").one_or_none()


def test_edit_new_item(client, session):
    data = {
        'item_id': 4,
        'new_item_name': "Samsung Galaxy S22"
    }

    result = client.post(
        '/edit_item',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )

    json_result = json.loads(result.data)

    assert json_result['status'] is True
    assert session.query(Item).filter_by(item_name="Samsung Galaxy S22").one_or_none()


def test_delete_item(client, session):
    data = {
        'item_id': 4
    }

    result = client.post(
        '/delete_item',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )

    json_result = json.loads(result.data)

    assert json_result['status'] is True
    assert session.query(Item).filter_by(item_name="Samsung Galaxy S22").one_or_none() is None
