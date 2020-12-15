<template>
  <!-- HEADER -->
  <header id="main-header" class="py-2 bg-warning text-white">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h1><i class="fas fa-users"></i> Users</h1>
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
        <div class="col">
          <div class="card">
            <div class="card-header">
              <h4>Latest Users</h4>
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
                <tr>
                  <td>1</td>
                  <td>John Doe</td>
                  <td>jdoe@gmail.com</td>
                  <td>
                    <a href="/profile" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right"></i> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Harry White</td>
                  <td>harry@yahoo.com</td>
                  <td>
                    <a href="/profile" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right"></i> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Mary Johnson</td>
                  <td>mary@gmail.com</td>
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
