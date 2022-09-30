<template>
    <div class="addBook_user">
        <div class="container_addBook_user">
        <h2>Añadir Libro</h2>
        <form v-on:submit.prevent="processAddBook" >    
            <input autocomplete="off" type="text" v-model="product.name_prod" placeholder="Nombre Producto">
            <br>
            <input autocomplete="off" type="text" v-model="product.author" placeholder="Nombre Autor">
            <br>
            <input autocomplete="off" type="text" v-model="product.editorial" placeholder="Editorial">
            <br>
            <input autocomplete="off" type="text" v-model="product.category" placeholder="Categoría">
            <br>
            <input autocomplete="off" type="text" v-model="product.type_prod" placeholder="Tipo Producto">
            <br>
            <input autocomplete="off" type="text" v-model="product.num_page" placeholder="Número de Páginas">
            <br>
            <input autocomplete="off" type="text" v-model="product.isbn" placeholder="Ingrese el ISBN">
            <br>
            <input autocomplete="off" type="text" v-model="product.state" placeholder="Estado">
            <br>
            <input autocomplete="off" type="text" v-model="product.rank" placeholder="Rango">
            <br>
            <input autocomplete="off" type="text" v-model="product.format_prod" placeholder="Formato Producto">
            <br>
            <input autocomplete="off" type="text" v-model="product.presentation" placeholder="Presentación">
            <br>
            <input autocomplete="off" type="text" v-model="product.image" placeholder="Imagen">
            <br>
            <input autocomplete="off" type="text" v-model="product.price" placeholder="Ingrese el Precio">
            <br>            
            <input autocomplete="off" type="text" v-model="product.description" placeholder="Descripción">
            <br>
            <input autocomplete="off" type="text" v-model="product.name_cat" placeholder="Nombre Categoría">
            <br>
            <input autocomplete="off" type="text" v-model="product.subcategory" placeholder="SubCategoría">
            <br>
            <input autocomplete="off" type="text" v-model="product.inventory_id" placeholder="Id Inventario">
            <br>
            <input autocomplete="off" type="text" v-model="product.sale_id" placeholder="Id Venta">
            <br>
            <input autocomplete="off" type="text" v-model="product.user_id" placeholder="Id Usurio">
            <br>
            <button type="submit">Añadir</button>
        </form>
        </div>
    </div>
    </template>
    <script>
    import axios from 'axios';
    export default {
        name: "AddBook",
        data: function(){
            return {
                product: {

                    name_prod: "",
                    author: "",
                    editorial: "",
                    category: "",
                    type_prod: "",
                    num_page: "",
                    isbn: "",
                    state: "",
                    rank: "",
                    format_prod: "",
                    presentation: "",
                    image: "",
                    price: "",
                    description: "",
                    name_cat: "",
                    subcategory: "",
                    inventory_id: "",
                    sale_id: "",
                    user_id: ""

                    // username: "",
                    // password: "",
                    // name: "",
                    // email: "",
                    // account: {
                    //     lastChangeDate: (new Date()).toJSON().toString(),
                    //     balance: 0,
                    //     isActive: true
                    // }
                }
            }
        },
        methods: {
            processAddBook: function(){
                axios.post(
                    "http://127.0.0.1:8000/products/",
                    this.product,
                    {headers: {}}
                )
    
            .then((result) => {
                let dataAddBook = {
                    product: this.product.name_prod,
                    author: this.product.author,
                    editorial: this.product.editorial,
                    category: this.product.category,
                    type_prod: this.product.type_prod,
                    num_page: this.product.num_page,
                    isbn: this.product.isbn,
                    state: this.product.state,
                    rank: this.product.rank,
                    format_prod: this.product.format_prod,
                    presentation: this.product.presentation,
                    image: this.product.image,
                    price: this.product.price,
                    description: this.product.description,
                    name_cat: this.product.name_cat,
                    subcategory: this.product.subcategory,
                    inventory_id: this.product.inventory_id,
                    sale_id: this.product.sale_id,
                    user_id: this.product.user_id

                    // username: this.user.username,
                    // token_access: result.data.access,
                    // token_refresh: result.data.refresh,
                }
                this.$emit('completedAddBook', dataAddBook)
            })
    
            .catch((error) => {
                console.log(error);
                alert(error, "ERROR: Fallo en el registro de libros.");
            });
            },
            verifyToken: function () {
                return axios.post("http://127.0.0.1:8000/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}}
            )
            .then((result) => {
                localStorage.setItem("token_access", result.data.access);
            })
            .catch(() => {
                this.$emit('logOut');
            });
            }
        }
    }
    </script>
    
    <style>
    .addBook_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .container_addBook_user {
        border: 3px solid #283747;
        border-radius: 10px;
        width: 35%;
        height: 80%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;}
    
    .addBook_user h2{
        color: #283747;
    }
    
    .addBook_user form{
        width: 70%;
    }
    
    .addBook_user input{
        height: 40px;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px0;
        border: 1px solid #283747;
    }
    
    .addBook_user button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px0 25px0;
    }
    
    .addBook_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }
    </style>