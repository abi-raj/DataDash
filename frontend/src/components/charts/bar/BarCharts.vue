<template>
  <div>
    <div class="all-charts">
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'basic' }"
        id="basic"
        @click="select('basic')"
      >
        Basic
      </div>
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'grouped' }"
        id="grouped"
        @click="select('grouped')"
      >
        Grouped
      </div>
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'labeled' }"
        id="labeled"
        @click="select('labeled')"
      >
        Data labeled
      </div>
    </div>
    <BarBasic v-if="choosen === 'basic'" />
    <BarGrouped v-if="choosen === 'grouped'" />
    <BarLabeled v-if="choosen === 'labeled'" />
  </div>
</template>

<script>
import BarBasic from "./BarBasic.vue";
import BarGrouped from "./BarGrouped.vue";
import BarLabeled from "./BarLabeled.vue";
export default {
  name: "BarCharts",
  components: {
    BarBasic,
    BarGrouped,
    BarLabeled
  },
  data() {
    return {
      choosen: null,
    };
  },
  methods: {
    select(name) {
      this.choosen = name;
      console.log(this.choosen);
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