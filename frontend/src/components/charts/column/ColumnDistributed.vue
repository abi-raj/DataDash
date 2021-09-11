<template>
  <div>
    <div class="chart-options">
      <div class="class_x">
        <label for="choose_x">Choose X axis : </label>
        <select
          name="choose_x"
          id="choose_x"
          class="border-4 border-green-300"
          @change="updateX"
        >
          <option v-for="str in fileData.strCols" :key="str">
            {{ str }}
          </option>
        </select>
      </div>
      <div class="class_y">
        <label for="choose_y">Choose Y axis : </label>
        <select
          name="choose_y"
          id="choose_y"
          class="border-4 border-green-300"
          @change="updateY"
        >
          <option v-for="number in fileData.numCols" :key="number">
            {{ number }}
          </option>
        </select>
      </div>

      <div class="rstart">
        <label for="rstart">Range Start : </label>
        <input
          type="number"
          v-model="start"
          class="border-4 border-green-300"
        />
      </div>

      <div class="rend">
        <label for="rend">Range End : </label>
        <input type="number" v-model="end" class="border-4 border-green-300" />
      </div>
    </div>
    <div id="chart">
      <apexchart
      ref="real"
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
import { mapState } from "vuex";
export default {
  name: "ColumnDistributed",
  components: {
    apexchart: VueApexCharts,
  },
   computed: {
    ...mapState(["fileData"]),
  },
  methods: {
    updateX(e) {
      console.log(this.start, this.end);

      this.$refs.real.updateOptions({
        xaxis: {
          categories: this.fileData.allData[e.target.value].slice(
            this.start,
            this.end
          ),
        },
      });
    },
    updateY(e) {
      this.$refs.real.updateSeries(
        [
          {
            name:e.target.value,
            data: this.fileData.allData[e.target.value].slice(
              this.start,
              this.end
            ),
          },
        ],
        false,
        true
      );
    },
  },
  data() {
    return {
      series: [],
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