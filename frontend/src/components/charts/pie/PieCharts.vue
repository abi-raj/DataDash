<template>
  <div>
    <div class="all-charts">
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'simple' }"
        id="simple"
        @click="select('simple')"
      >
        Simple Pie
      </div>
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'donut' }"
        id="donut"
        @click="select('donut')"
      >
        Simple Donut
      </div>
 <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'mono' }"
        id="mono"
        @click="select('mono')"
      >Mono Pie
      </div>

    </div>

  </div>
</template>

<script>

export default {
  name: "PieCharts",

  data() {
    return {
      choosen: null,
    };
  },
  methods: {
    select(name) {
      console.log("clicked");
      this.choosen = name;
    },
  },
};
</script>

<style >
.chart-select{
  @apply border-2 p-2 w-1/12 text-center;
}
.all-charts{
  @apply p-4 flex justify-around;
}
</style>