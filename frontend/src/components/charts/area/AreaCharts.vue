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
      >Date Timed
      </div>

    </div>

  </div>
</template>

<script>

export default {
  name: "AreaCharts",

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