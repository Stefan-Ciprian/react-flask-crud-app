import React, {Component} from 'react';
import axios from "axios";
import { MdModeEdit, MdDelete } from 'react-icons/md'
import './App.css';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            items: [],
            categories: [],
            currentCategoryId: 1,
            editItemName: ""
        };

        this.handleChange = this.handleChange.bind(this);
        this.closeAlert = this.closeAlert.bind(this);
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

    editItem(id) {
        const result = window.confirm("Are you sure you want to edit this item?");

        if (result) {
            axios.post('/edit_item', {
                'item_id': id,
                'new_item_name': this.state.editItemName
            }).then(response => {
                console.log(response.data);
                this.getItems(this.state.currentCategoryId);
            }).catch(function (error) {
                console.log(error);
            });
        }
    }

    deleteItem(id) {
        this.getItems(id);
    }

    handleChange(e) {
        this.setState({ editItemName: e.target.value });
    }

    closeAlert() {
        alert('closed');
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
                    <div className="row">
                        <div className="col-10 mt-1">
                            <div>
                                <input className="form-control" type="text" defaultValue={item['item_name']} onChange={this.handleChange} />
                            </div>
                        </div>
                        <div className="col-2">
                            <button type="button" className="btn btn-default btn-sm"
                                    onClick={() => this.editItem(item['id'])}>
                                <MdModeEdit size={20}/>
                            </button>
                            <button type="button" className="btn btn-default btn-sm"
                                    onClick={() => this.deleteItem(item['id'])}>
                                <MdDelete size={20}/>
                            </button>
                        </div>
                    </div>
                </li>
            )
        });

        return (
            <div className="container">
                <div className="row main-row">
                    <div className="col-4 main-col">
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
                    </div>
                    <div className="col-8 main-col">
                        <div className="alert alert-warning alert-dismissible fade show" role="alert">
                            <strong>Holy guacamole!</strong> You should check in on some of those fields below.
                            <button type="button" className="close" onClick={this.closeAlert}>
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                         <ul className="list-group">
                             {items}
                        </ul>
                    </div>
                </div>
            </div>
        )
    }
}

export default App;