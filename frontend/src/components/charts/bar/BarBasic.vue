<template>
    <div>
        <div class="row">
        choose x dropdown ,
        choose y dropdown ,
        </div>
        <div class="chart">
            <apexchart type="bar" height="350" :options="chartOptions" :series="series"></apexchart>
        </div>
    </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";
    export default {
        name: 'BarBasic',
        components: {
        apexchart: VueApexCharts,
        },

          data() {
          
        return {
              series: [{
            data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380],
           
          }],
          chartOptions: {
               colors:[ '#9C27B0'],
            chart: {
              type: 'bar',
              height: 350
            },
            plotOptions: {
              bar: {
                borderRadius: 4,
                horizontal: true,
              }
            },
            dataLabels: {
              enabled: false
            },
            xaxis: {
              categories: ['South Korea', 'Canada', 'United Kingdom', 'Netherlands', 'Italy', 'France', 'Japan',
                'United States', 'China', 'Germany'
              ],
            }
          },
        }
          
          
        },
    }
</script>

<style >

</style>