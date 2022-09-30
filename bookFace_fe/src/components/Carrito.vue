<template>
    <div  class="information">
        <h1>Información del libro</h1>
        <h2>Nombre: <span>{{name_prod}}</span></h2>
        <h2>precio: <span>{{price}} COP </span></h2>
        <h2>autor: <span>{{author}}</span></h2>
    </div>
</template>

<script>
   import jwt_decode from "jwt-decode";
   import axios from 'axios';
   export default {
    name: "Products",
    data: function(){
        return {
            name_prod: "",
            author: "",
            price: 0,
            loaded: false,
        }
    },
    methods: {
        getData: async function () {
            if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
            this.$emit('logOut');
            return;
    }
            await this.verifyToken();
            let token = localStorage.getItem("token_access");
            
            axios.get(`http://127.0.0.1:8000/products/1/`, {headers: {'Authorization': `Bearer ${token}`}})
                .then((result) => {
                    this.name_prod = result.data.name_prod;
                    this.author = result.data.author;
                    this.price = result.data.price;
                    this.loaded = true;
                })
                    .catch((e) => {
                        alert (e)
                        this.$emit('logOut');
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
    },
 created: async function(){
 this.getData();
 },
}
</script>
<style>
 .information{
 margin: 0;
 padding: 0%;
 width: 100%;
 height: 100%;
 display: flex;
 flex-direction: column;
 justify-content: center;
 align-items: center;
 }
 information h1{
    font-size: 60px;
    color: #0f1316;
    }
    .information h2{
    font-size: 40px;
    color: #283747;
    }
    .information span{
    color: crimson;
    font-weight: bold;
    }
   </style>