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
        :class="{ 'border-green-300': choosen === 'spline' }"
        id="spline"
        @click="select('spline')"
      >
        Spline
      </div>
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'datetime' }"
        id="datetime"
        @click="select('datetime')"
      >
        Date Timed
      </div>
    </div>
    <div class="charts">
      <AreaBasic v-if="choosen === 'basic'" />
      <AreaSpline v-if="choosen === 'spline'" />
    </div>
  </div>
</template>

<script>
import AreaBasic from "./AreaBasic.vue";
import AreaSpline from "./AreaSpline.vue";
export default {
  name: "AreaCharts",
  components: {
    AreaBasic,
    AreaSpline,
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