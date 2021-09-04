<template>
  <div class="container mx-auto p-10">
    <div class="w-auto flex flex-row justify-between">
      <div><h2 class="text-xl">1) Load File</h2></div>
      <div>
        <select class="border-4 border-green-300">
          <option value="">File</option>
          <option value="">URL</option>
          <option value="">PRESETS</option>
        </select>
      </div>
    </div>
    <div
      class="
        w-auto
        border-4 border-green-300 border-dashed
        container
        bg-green-100
        p-10
        mt-10
        rounded
      "
      @dragover.prevent="handleDragOver"
      @drop.prevent="handleDrop"
      @dragleave.prevent="handleDragLeave"
    >
      <div class="flex flex-col content-center items-center">
        <p class="m-center text-2xl">Drop a file here</p>

        <p class="m-center text-xl mt-1">or</p>

        <label for="chooseFile" class="rounded-lg p-3 bg-green-300 mt-2"
          >Choose File</label
        >
        <input type="file" id="chooseFile" class="m-center w-0 h-0" @change="chooseFile" />
        <div class="showFile rounded bg-red-400 mt-3 p-1" v-if="fileSelected">
          <p class="m-center text-white">{{fileSelected.name}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoadFile",
  data(){
    return {
      fileSelected:null,
    }
  },
  methods: {
    handleDragOver() {
      console.log("dragging");
    },
    handleDrop(event) {
      console.log("dropped");
    this.fileSelected = event.dataTransfer.items[0].getAsFile();

    },
    handleDragLeave() {
      console.log("mouse left");
    },
    chooseFile(event) {
      console.log("file selected");
      this.fileSelected = event.target.files[0];
      console.log(this.fileSelected);
    },
  },
};
</script>

<style >
</style>