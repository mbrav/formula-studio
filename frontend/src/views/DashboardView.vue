<template>
  <!-- HEADER -->
  <header id="main-header" class="py-2 bg-primary text-white">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h1><i class="fas fa-cog" /> Dashboard</h1>
        </div>
      </div>
    </div>
  </header>

  <!-- ACTIONS -->
  <section id="actions" class="py-4 mb-4 bg-light">
    <div class="container">
      <div class="row">
        <div class="col-md-3">
          <a
            href="#"
            class="btn btn-primary btn-block"
            data-bs-toggle="modal"
            data-bs-target="#addClassModal"
          >
            <i class="fas fa-plus" /> Class Signup
          </a>
        </div>
        <div class="col-md-3">
          <a
            href="#"
            class="btn btn-success btn-block"
            data-bs-toggle="modal"
            data-bs-target="#addCategoryModal"
          >
            <i class="fas fa-plus" /> Add Category
          </a>
        </div>
        <div class="col-md-3">
          <a
            href="#"
            class="btn btn-warning btn-block"
            data-bs-toggle="modal"
            data-bs-target="#addUserModal"
          >
            <i class="fas fa-plus" /> Add User
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- POSTS -->
  <section id="posts">
    <div class="container">
      <div class="row">
        <div class="col-md-9">
          <div class="card">
            <div class="card-header">
              <h4>Latest Classes</h4>
            </div>
            <table class="table table-striped">
              <thead class="thead-dark">
                <tr>
                  <th>#</th>
                  <th>Title</th>
                  <th>Category</th>
                  <th>Date</th>
                  <th />
                </tr>
              </thead>
              <tbody>
                <tr v-for="group in groups" :key="group">
                  <td>{{ group.id }}</td>
                  <td>{{ group.name }}</td>
                  <td>{{ group.category }}</td>
                  <td>{{ ClassDate(group.date) }}</td>
                  <td>
                    <a href="details.html" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="col-md-3">
          <div class="card text-center bg-primary text-white mb-3">
            <div class="card-body">
              <h3>Classes</h3>
              <h4 class="display-4">
                <i class="fas fa-pencil-alt" /> {{ groups.length }}
              </h4>
              <a href="/classes" class="btn btn-outline-light btn-sm">View</a>
            </div>
          </div>

          <div class="card text-center bg-success text-white mb-3">
            <div class="card-body">
              <h3>Signups</h3>
              <h4 class="display-4">
                <i class="fas fa-folder" /> {{ groups.length }}
              </h4>
              <a href="/categories" class="btn btn-outline-light btn-sm"
                >View</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MODALS -->

  <!-- SIGNUP FOR CLASS MODAL -->
  <div class="modal fade" id="addClassModal">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header bg-primary text-white">
          <h5 class="modal-title">Signup for class</h5>
          <button class="close" data-bs-dismiss="modal">
            <span>&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="title">Title</label>
              <input type="text" class="form-control" />
            </div>
            <div class="form-group">
              <label for="category">Category</label>
              <select class="form-control">
                <option value="">Yoga</option>
                <option value="">Hot Yoga</option>
                <option value="">Health & Wellness</option>
              </select>
            </div>
            <div class="form-group">
              <label for="body">Body</label>
              <textarea name="editor1" class="form-control" />
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary" data-bs-dismiss="modal">
            Save Changes
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ADD CATEGORY MODAL -->
  <div class="modal fade" id="addCategoryModal">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header bg-success text-white">
          <h5 class="modal-title">Add Category</h5>
          <button class="close" data-bs-dismiss="modal">
            <span>&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="title">Title</label>
              <input type="text" class="form-control" />
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="btn btn-success" data-bs-dismiss="modal">
            Save Changes
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ADD USER MODAL -->
  <div class="modal fade" id="addUserModal">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header bg-warning text-white">
          <h5 class="modal-title">Add User</h5>
          <button class="close" data-bs-dismiss="modal">
            <span>&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="name">Name</label>
              <input type="text" class="form-control" />
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" class="form-control" />
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input type="password" class="form-control" />
            </div>
            <div class="form-group">
              <label for="password2">Confirm Password</label>
              <input type="password" class="form-control" />
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="btn btn-warning" data-bs-dismiss="modal">
            Save Changes
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var moment = require("moment");

export default {
  name: "DashboardView",
  components: {},
  props: {},
  data() {
    return {};
  },
  computed: {
    groups() {
      return this.$store.state.groupData;
    },
  },
  methods: {
    ClassDate(date) {
      return moment(date).format("MMM Do YYYY");
    },
  },
  mounted() {
    this.$store.dispatch("getGroups");
  },
};
</script>

<style scoped lang="scss"></style>
