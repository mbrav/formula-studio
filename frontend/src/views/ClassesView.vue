<template>
  <!-- HEADER -->
  <header id="main-header" class="py-2 bg-primary text-white">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h1><i class="fas fa-pencil-alt" /> Classes</h1>
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
              placeholder="Search Classes..."
            />
            <div class="input-group-append">
              <button class="btn btn-primary">Search</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- POSTS -->
  <section id="posts">
    <div class="container">
      <div class="row">
        <div class="col">
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
                <tr>
                  <td>1</td>
                  <td>Class One</td>
                  <td>Web Development</td>
                  <td>May 10 2018</td>
                  <td>
                    <a href="/class-details" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Class Two</td>
                  <td>Tech Gadgets</td>
                  <td>May 11 2018</td>
                  <td>
                    <a href="/class-details" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Class Three</td>
                  <td>Web Development</td>
                  <td>May 13 2018</td>
                  <td>
                    <a href="/class-details" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Class Four</td>
                  <td>Business</td>
                  <td>May 15 2018</td>
                  <td>
                    <a href="/class-details" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Class Five</td>
                  <td>Web Development</td>
                  <td>May 17 2018</td>
                  <td>
                    <a href="/class-details" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>Class Six</td>
                  <td>Health & Wellness</td>
                  <td>May 20 2018</td>
                  <td>
                    <a href="/class-details" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
              </tbody>
            </table>

            <!-- PAGINATION -->
            <nav class="ml-4">
              <ul class="pagination">
                <li class="page-item disabled">
                  <a href="#" class="page-link">Previous</a>
                </li>
                <li class="page-item active">
                  <a href="#" class="page-link">1</a>
                </li>
                <li class="page-item">
                  <a href="#" class="page-link">2</a>
                </li>
                <li class="page-item">
                  <a href="#" class="page-link">3</a>
                </li>
                <li class="page-item">
                  <a href="#" class="page-link">Next</a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// import axios from "axios";
export default {
  name: "ClassesView",
  props: {
    msg: String,
  },
  // mounted() {
  //   axios.get("http://localhost:8000/api/v1/groups/").then(response => {
  //     console.log(response.data);
  //   });
  // }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped></style>
