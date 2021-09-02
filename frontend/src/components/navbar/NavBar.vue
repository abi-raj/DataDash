<template>
  <div>
    <nav class="bg-green-50 p-5 px-10">
      <div class="max-w mx-auto">
        <div class="flex justify-between">
          <!-- nav items -->
          <div class="flex">
            <!-- Logo -->
            <div>
              <a href="#" class="flex space-x-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6 mt-1"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13 10V3L4 14h7v7l9-11h-7z"
                  />
                </svg>
                <span class="text-lg">Data-Dash</span>
              </a>
            </div>
          </div>
          <!-- nav last items -->
          <div class="flex space-x-10">
            <a href="#" class="nav-item">About</a>
            <a href="#" class="nav-item">GitHub</a>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style >

.nav-item{
    @apply hover:bg-green-100  px-3 py-1 rounded-lg;
}

</style>