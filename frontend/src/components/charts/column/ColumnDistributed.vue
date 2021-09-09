<template>
  <div>
    <div id="chart">
      <apexchart
        type="bar"
        height="350"
        :options="chartOptions"
        :series="series"
      ></apexchart>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";
export default {
  name: "ColumnDistributed",
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [{
            data: [21, 22, 10, 28, 16, 21, 13, 30]
          }],
          chartOptions: {
            chart: {
              height: 350,
              type: 'bar',
              events: {
                click: function(chart, w, e) {
                 console.log(chart, w, e)
                }
              }
            },
           
            plotOptions: {
              bar: {
                columnWidth: '45%',
                distributed: true,
              }
            },
            dataLabels: {
              enabled: false
            },
            legend: {
              show: false
            },
            xaxis: {
              categories: [
                ['John', 'Doe'],
                ['Joe', 'Smith'],
                ['Jake', 'Williams'],
                'Amber',
                ['Peter', 'Brown'],
                ['Mary', 'Evans'],
                ['David', 'Wilson'],
                ['Lily', 'Roberts'], 
              ],
              labels: {
                style: {
                 
                  fontSize: '12px'
                }
              }
            }
          },
          
    };
  },
};
</script>

<style >
</style>