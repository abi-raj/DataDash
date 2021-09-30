<template>
  <div class="chart-wrapper">
    <apexchart width="500" type="bar" :options="options" :series="series">
    </apexchart>
  </div>
</template>
<script>
import VueApexCharts from "vue3-apexcharts";

export default {
  name: "HelloWorld",
  props: ["xax", "yax"],
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      options: {
        chart: {
          id: "vuechart-example",
        },
        xaxis: {
          categories: this.xax.slice(1,10),
        },
      },
      series: [
        {
          name: "series-1",
          data: this.yax.slice(1,10),
        },
      ],
    };
  },
};
</script>

<style scoped>
div.chart-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>