import React, {Component} from 'react';
import axios from "axios";
import { MdModeEdit, MdDelete, MdAdd } from 'react-icons/md'
import './App.css';
import {Col, Container, Row} from "react-bootstrap";
import Alert from 'react-bootstrap/Alert';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            items: [],
            categories: [],
            currentCategoryId: 1,
            editItemName: "",
            insertItemName: "",
            showAlert: false,
            showAddForm: false,
            alertText: ""
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleInsertChange = this.handleInsertChange.bind(this);
    }

    componentDidMount() {
        this.getCategories();
        this.getItems(this.state.currentCategoryId);
    }

    getCategories() {
        axios.get('/get_categories')
        .then(response => {
            this.setState({
                categories: response.data.categories
            });
        });
    }

    getItems(category_id) {
        axios.get(`/get_items/${category_id}`)
        .then(response => {
            this.setState({
                items: response.data.items
            });
        });
    }

    setCategory(id) {
        this.setState({ currentCategoryId: id });
        this.getItems(id);
    }

    insertItem() {
        const result = window.confirm("Are you sure you want to insert this item?");

        if (result) {
            axios.post('/insert_item', {
                'category_id': this.state.currentCategoryId,
                'item_name': this.state.insertItemName
            }).then(response => {
                this.setState({
                    showAlert: true,
                    alertText: "Item inserted!",
                    showAddForm: false
                });
                this.getItems(this.state.currentCategoryId);
            }).catch(function (error) {
                console.log(error);
            });
        }
    }

    editItem(id, itemName) {
        const result = window.confirm("Are you sure you want to edit this item?");

        if (result) {
            axios.post('/edit_item', {
                'item_id': id,
                'new_item_name': this.state.editItemName ? this.state.editItemName : itemName
            }).then(response => {
                this.setState({
                    showAlert: true,
                    alertText: "Item edited!"
                });
                this.getItems(this.state.currentCategoryId);
            }).catch(function (error) {
                console.log(error);
            });
        }
    }

    deleteItem(id) {
        const result = window.confirm("Are you sure you want to delete this item?");

        if (result) {
            axios.post('/delete_item', {
                'item_id': id
            }).then(response => {
                this.setState({
                    showAlert: true,
                    alertText: "Item deleted!"
                });
                this.getItems(this.state.currentCategoryId);
            }).catch(function (error) {
                console.log(error);
            });
        }
    }

    handleChange(e) {
        this.setState({ editItemName: e.target.value });
    }

    handleInsertChange(e) {
        this.setState({ insertItemName: e.target.value });
    }

    setShow(value) {
        this.setState({ showAlert: value });
    }

    showAdd() {
        this.setState({ showAddForm: !this.state.showAddForm });
    }

    render() {
        const categories = this.state.categories.map((category) => {
            return (
                <li className="nav-item">
                    <button className={this.state.currentCategoryId === category['id'] ? "nav-link active" : "nav-link text-white"} onClick={() => this.setCategory(category['id'])} >{category['category_name']}</button>
                </li>
                )
            }
        );

        const items = this.state.items.map((item) => {
            return (
                <li className="list-group-item" key={item['id']}>
                    <Row>
                        <Col xs={7} md={8} lg={10}>
                            <div>
                                <input className="form-control" type="text" defaultValue={item['item_name']} onChange={this.handleChange} />
                            </div>
                        </Col>
                        <Col xs={5} md={4} lg={2}>
                            <button type="button" className="btn btn-default btn-sm"
                                    onClick={() => this.editItem(item['id'], item['item_name'])}>
                                <MdModeEdit size={20}/>
                            </button>
                            <button type="button" className="btn btn-default btn-sm"
                                    onClick={() => this.deleteItem(item['id'])}>
                                <MdDelete size={20}/>
                            </button>
                        </Col>
                    </Row>
                </li>
            )
        });

        return (
            <Container>
                <Row>
                    <Col sm={4} className="main-col">
                        <div className="main">
                            <div className="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark">
                                <a href="/" className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                                    <span className="fs-4">Categories</span>
                                </a>
                                <hr />
                                    <ul className="nav nav-pills flex-column mb-auto">
                                        {categories}
                                    </ul>
                            </div>
                        </div>
                    </Col>
                    <Col sm={8} className="main-col">
                        { this.state.showAlert ?
                            <Alert className="mt-3" variant="success" onClose={() => this.setShow(false)} dismissible>
                                <Alert.Heading>{this.state.alertText}</Alert.Heading>
                            </Alert>
                            : ""}
                         <ul className="list-group">
                             {items}
                        </ul>
                        <Row>
                            <Col sm={6}>
                                <button type="button" className="btn btn-default"
                                    onClick={() => this.showAdd()}><MdAdd size={20}/> Add item
                                </button>
                            </Col>
                        </Row>
                        { this.state.showAddForm ?
                            <Row>
                                <Col>
                                    <Row className="mt-2">
                                        <Col sm={6}>
                                            <input className="form-control" type="text" defaultValue="" onChange={this.handleInsertChange} />
                                        </Col>
                                    </Row>
                                    <Row className="mt-2">
                                        <Col>
                                            <button type="button" className="btn btn-default btn-primary"
                                            onClick={() => this.insertItem()}>Save item
                                        </button>
                                        </Col>
                                    </Row>
                                </Col>
                            </Row>
                            : ""}
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default App;