<template>
  <!-- HEADER -->
  <header id="main-header" class="py-2 bg-success text-white">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h1><i class="fas fa-folder" /> Categories</h1>
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
              placeholder="Search Categories..."
            />
            <div class="input-group-append">
              <button class="btn btn-success">
                Search
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CATEGORIES -->
  <section id="categories">
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-header">
              <h4>Latest Categories</h4>
            </div>
            <table class="table table-striped">
              <thead class="thead-dark">
                <tr>
                  <th>#</th>
                  <th>Title</th>
                  <th>Date</th>
                  <th />
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>Yoga</td>
                  <td>November 10 2020</td>
                  <td>
                    <a href="details.html" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Stretching</td>
                  <td>November 11 2020</td>
                  <td>
                    <a href="details.html" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Hot Yoga</td>
                  <td>November 13 2020</td>
                  <td>
                    <a href="details.html" class="btn btn-secondary">
                      <i class="fas fa-angle-double-right" /> Details
                    </a>
                  </td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Meditation</td>
                  <td>November 15 2020</td>
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
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "CategoriesView",
  props: {
    msg: String
  }
};
</script>

<style lang="scss" scoped></style>
