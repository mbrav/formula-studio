<template>
  <!-- HEADER -->
  <header id="main-header" class="py-2 bg-warning text-white">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h1><i class="fas fa-users"></i> Instructors</h1>
        </div>
      </div>
    </div>
  </header>

  <!-- SEARCH -->
  <section id="search" class="py-4 mb-4 bg-light">
    <div class="container">
      <div class="row">
        <div class="col-md-6 ml-auto">
          <div class="input-group">
            <input
              type="text"
              class="form-control"
              placeholder="Search Users..."
            />
            <div class="input-group-append">
              <button class="btn btn-warning">Search</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- USERS -->
  <section id="users">
    <div class="container">
      <div class="row">
        <div class="col-md-9">
          <div class="card">
            <div class="card-header">
              <h4>Instructors</h4>
            </div>
            <table class="table table-striped">
              <thead class="thead-dark">
                <tr>
                  <th>#</th>
                  <th>Name</th>
                  <th>Email</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="instructor in instructorData" :key="instructor">
                  <td>{{ instructor.id }}</td>
                  <td>
                    {{ instructor.first_name + " " + instructor.last_name }}
                  </td>
                  <td>{{ instructor.email }}</td>
                  <td>
                    <a href="/profile" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right"></i> Details
                    </a>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="col-md-3">
          <div class="card text-center bg-warning text-white mb-3">
            <div class="card-body">
              <h3>Instructors</h3>
              <h4 class="display-4">
                <i class="fas fa-users" /> {{ instructorData.length }}
              </h4>
              <a href="/users" class="btn btn-outline-light btn-sm">View</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "UsersView",
  props: {
    msg: String,
  },
};
</script>

<style lang="scss" scoped></style>
