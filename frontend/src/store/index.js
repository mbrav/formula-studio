import { createStore } from "vuex";
import axios from "axios";

var APIroot = "http://localhost:8000/api/v1/";

export default createStore({
  state: {
    groupData: [],
    instructorData: [],
    memberData: [],
    signupData: [],
    PaymentData: [],
    subscriptionData: [],
    subscriptionVisitData: [],
    SingleVisitData: [],
    PurchaseData: [],
  },
  mutations: {
    SET_STATE_GROUPS(state, data) {
      state.groupData = data;
    },
    SET_STATE_INSTRUCTORS(state, data) {
      state.instructorData = data;
    },
    SET_STATE_MEMBERS(state, data) {
      state.memberData = data;
    },
    SET_STATE_SIGNUPS(state, data) {
      state.signupData = data;
    },
    SET_STATE_PAYMENTS(state, data) {
      state.PaymentData = data;
    },
    SET_STATE_SUBSCRIPTIONS(state, data) {
      state.subscriptionData = data;
    },
    SET_STATE_SUBSCRIPTION_VISITS(state, data) {
      state.subscriptionVisitData = data;
    },
    SET_STATE_SINGLE_VISITS(state, data) {
      state.SingleVisitData = data;
    },
    SET_STATE_PURCHASES(state, data) {
      state.PurchaseData = data;
    },
  },
  actions: {
    getGroups({ commit }) {
      axios.get(APIroot + "groups/").then((response) => {
        commit("SET_STATE_GROUPS", response.data);
      });
    },
    getInstructors({ commit }) {
      axios.get(APIroot + "instructors/").then((response) => {
        commit("SET_STATE_INSTRUCTORS", response.data);
      });
    },
    getMembers({ commit }) {
      axios.get(APIroot + "members/").then((response) => {
        commit("SET_STATE_MEMBERS", response.data);
      });
    },
    getSignups({ commit }) {
      axios.get(APIroot + "signups/").then((response) => {
        commit("SET_STATE_SIGNUPS", response.data);
      });
    },
    getPayments({ commit }) {
      axios.get(APIroot + "payments/").then((response) => {
        commit("SET_STATE_PAYMENTS", response.data);
      });
    },
    getSubscriptions({ commit }) {
      axios.get(APIroot + "subscriptions/").then((response) => {
        commit("SET_STATE_SUBSCRIPTIONS", response.data);
      });
    },
    getSubscriptionVisits({ commit }) {
      axios.get(APIroot + "subscription-visits/").then((response) => {
        commit("SET_STATE_SUBSCRIPTION_VISITS", response.data);
      });
    },
    getSingleVisits({ commit }) {
      axios.get(APIroot + "single-visits/").then((response) => {
        commit("SET_STATE_SINGLE_VISITS", response.data);
      });
    },
    getPurchases({ commit }) {
      axios.get(APIroot + "purchases/").then((response) => {
        commit("SET_STATE_GROUPS", response.data);
      });
    },
  },
  modules: {},
});
