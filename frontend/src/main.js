import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import moment from "moment";

// Dont import BootstrapVue for now
// See https://github.com/bootstrap-vue/bootstrap-vue/issues/5196

// import BootstrapVue from 'bootstrap-vue'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

import "bootstrap/scss/bootstrap.scss";
import "@fortawesome/fontawesome-free/css/all.min.css";

// TEMP, until BootstrapVue support for Vue3 is ready
import "bootstrap/dist/js/bootstrap.bundle.js";

const app = createApp(App);
app.use(moment);
app.use(store);
app.use(router);
// app.use(BootstrapVue)
app.mount("#app");
