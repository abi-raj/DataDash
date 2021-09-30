<template>
  <div>
    <div class="analyse-ops">
      <div class="class_y">
        <label for="choose_y">Choose a column : </label>
        <select
          name="choose_y"
          id="choose_y"
          class="border-4 border-green-300"
          v-model="selectedCol"
          @change="updateCol"
        >
          <option v-for="number in fileData.numCols" :key="number">
            {{ number }}
          </option>
        </select>
      </div>
    </div>

    <div class="summary-table flex justify-center align-center ">
      <table class="table-auto border border-collapse ">
        <thead>
          <tr>
            <th class="p-2">Function</th>
            <th class="p-2">Value</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="td-border">Minimum</td>
            <td class="td-border">{{numAnalysis.min}}</td>
          </tr>
          <tr class="bg-emerald-200">
            <td class="td-border">
             Maximum
            </td>
            <td class="td-border">{{numAnalysis.max}}</td>
          </tr>
          <tr>
            <td class="td-border">Average</td>
            <td class="td-border">{{numAnalysis.avg}}</td>
          </tr>
              <tr>
            <td class="td-border">Sum</td>
            <td class="td-border">{{numAnalysis.sum}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "AnalysisBase",
  computed:{
      ...mapState(["fileData"]),
  },
  data(){
      return {

          selectedCol:null,
          numAnalysis:{
                min:"-",
                max:"-",
                avg:"-",
                sum:"-",
          },
      }
  },
  methods: {
updateCol (e){
   
    this.numAnalysis.min = Math.min(...this.fileData.allData[e.target.value]);
    
    this.numAnalysis.max = Math.max(...this.fileData.allData[e.target.value]);
    this.numAnalysis.avg = (this.fileData.allData[e.target.value].reduce((a,b)=>a+b)/this.fileData.allData[e.target.value].length).toFixed(2);
    this.numAnalysis.sum = this.fileData.allData[e.target.value].reduce((a,b)=>a+b).toFixed(2);
}
  },
};
</script>

<style >
.analyse-ops {
  @apply p-5 flex flex-row justify-around;
}
.td-border{
    @apply border border-green-600 p-2 text-center;
}
</style>