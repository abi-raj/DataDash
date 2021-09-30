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
      >
        Mono Pie
      </div>
    </div>
    <div class="charts">
      <PieSimple v-if="choosen === 'simple'"></PieSimple>
      <PieDonut v-if="choosen === 'donut'"></PieDonut>
      <PieMono v-if="choosen === 'mono'"></PieMono>
    </div>
  </div>
</template>

<script>
import PieSimple from "./PieSimple.vue";
import PieDonut from "./PieDonut.vue";
import PieMono from "./PieMono.vue";
export default {
  name: "PieCharts",
  components: {
    PieSimple,
    PieDonut,
    PieMono,
  },
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
.chart-select {
  @apply border-2 p-2 w-1/12 text-center;
}
.all-charts {
  @apply p-4 flex justify-around;
}
</style>