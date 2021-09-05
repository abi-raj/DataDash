<template>
  <div>
    <NavBar />
    <LoadFile @updateToParent="updateFile" />
    <div v-if="fileData.columns">
      <DataInfo
        v-if="fileData.columns !== undefined"
        :cols="fileData.columns"
        :dtypes="fileData.dtypes"
        :rowSize="fileData.rowSize"
        :totalSize="fileData.totalSize"
      />
    </div>
    <div  v-if="fileData.columns" class="choice flex justify-center">
     <div  class="ml-4 space-x-2"> <input type="radio" id="charts" value="charts" v-model="picked" />
      <label for="charts">Charts</label></div>
     
      <div  class="ml-4 space-x-2"><input type="radio" id="analytics" value="analytics" v-model="picked" />
      <label for="analytics">Analytics</label></div>
     
    </div>
  </div>
</template>

<script>
import NavBar from "./navbar/NavBar.vue";
import LoadFile from "./file/LoadFile.vue";
import DataInfo from "./file/DataInfo.vue";
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      yes: false,
      fileSelected: null,
      fileData: {
        allData: null,
        columns: null,
        dtypes: null,
        rowSize: null,
        totalSize: null,
      },
      picked:null,
    };
  },
  components: {
    NavBar,
    LoadFile,
    DataInfo,
  },
  methods: {
    updateFile(file) {
      if (file === null || file === undefined) {
        this.yes = false;
      } else {
        this.fileSelected = file;
        this.onUpload();
      }
    },
    onUpload() {
      const formData = new FormData();
      formData.append("file", this.fileSelected, this.fileSelected.name);
      axios
        .post(
          "https://CloudyPuzzledDominspector.abisnhss.repl.co/upload",
          formData
        )
        .then((response) => {
          this.fileData.columns = response.data.columns;
          this.fileData.allData = response.data;
          this.fileData.dtypes = response.data.dtypes;
          this.fileData.rowSize = response.data.rowSize;
          this.fileData.totalSize = response.data.totalSize;
          console.log(this.fileData.allData);
          this.yes = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style  scoped>
</style>