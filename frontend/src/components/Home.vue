<template>
  <div>
    <NavBar />

    <LoadFile @updateToParent="onUpload" />

    <div v-if="fileData.columns">
      <DataInfo
        v-if="fileData.columns !== undefined"
        :cols="fileData.columns"
        :dtypes="fileData.dtypes"
        :rowSize="fileData.rowSize"
        :totalSize="fileData.totalSize"
      />
    </div>

    <div class="choice flex justify-center"  v-if="fileData.columns">
     <div  class="ml-4 space-x-2"> <input type="radio" id="charts" value="charts" v-model="picked" @change="setDisplayType('charts')" />
      <label for="charts">Charts</label></div>
     
      <div  class="ml-4 space-x-2"><input type="radio" id="analytics" value="analytics" v-model="picked" @change="setDisplayType('analytics')"/>
      <label for="analytics">Analytics</label></div>
     
    </div>

   <div v-if="fileData.columns">
     
      <div v-if="picked === 'charts'">
     <ChooseChart />
      </div>

   </div>


  </div>
</template>

<script>
import NavBar from "./navbar/NavBar.vue";
import LoadFile from "./file/LoadFile.vue";
import DataInfo from "./file/DataInfo.vue";
import ChooseChart from "./charts/ChooseChart.vue";
import axios from "axios";
import { mapState ,mapMutations,mapGetters} from "vuex";
export default {
  name: "Home",
 
  computed: {
...mapState(["fileSelected","fileData","picked"]),
...mapGetters(["stringColumns","numberColumns"]),
  },
  components: {
    NavBar,
    LoadFile,
    DataInfo,
    ChooseChart
  },
  methods: {
    ...mapMutations(["setFileData","setDisplayType"]),
 
    onUpload() {
      if(this.fileSelected){
   const formData = new FormData();
      formData.append("file", this.fileSelected, this.fileSelected.name);
      axios
        .post(
          "https://CloudyPuzzledDominspector.abisnhss.repl.co/upload",
          formData
        )
        .then((response) => {
          console.log(response.data);
          this.setFileData(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
      }
   
    },

  },

};
</script>

<style  scoped>
</style>