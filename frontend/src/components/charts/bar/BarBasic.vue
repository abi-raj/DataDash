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
    <div class="chart">
      <apexchart
        ref="real"
        type="bar"
        height="500"
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
  name: "BarBasic",
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
      // console.log(e.target.value);
      // console.log(typeof this.fileData.allData[e.target.value]);
      // console.log(this.fileData.allData[e.target.value]);
      this.$refs.real.updateSeries(
        [
          {
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
      start: 0,
      end: 20,
      colX: this.fileData,
      colY: null,
      series: [
        {
          data: [],
        
        },
      ],
      chartOptions: {
        colors: ["#9C27B0"],
        chart: {
          type: "bar",
          height: 350,
        },
        plotOptions: {
          bar: {
            borderRadius: 4,
            horizontal: true,
          },
        },
        dataLabels: {
          enabled: false,
        },
        xaxis: {
          categories: [],
         
        },
      },
    };
  },
};
</script>

<style >
.chart-options{
  @apply  p-5 flex flex-row justify-around;
}

</style>