<template>
  <div>
    
    <div id="chart">
      <apexchart
        type="line"
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
  name: "LineStep",
  components: {
    apexchart: VueApexCharts,
  },
  data() {
      return{
            series: [{
            data: [34, 44, 54, 21, 12, 43, 33, 23, 66, 66, 58]
          }],
          
          
            chartOptions: {
            chart: {
              type: 'line',
              height: 350
            },
            stroke: {
              curve: 'stepline',
            },
            dataLabels: {
              enabled: false
            },
            title: {
              text: 'Stepline Chart',
              align: 'left'
            },
            markers: {
              hover: {
                sizeOffset: 4
              }
            }
          },
        
      }
  }
}

  

</script>

<style >
</style>