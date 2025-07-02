<contents>
<template>
  <div class="python-code">
    <pre><code class="language-python">
      <slot></slot>
    </code></pre>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  code: {
    type: String,
    required: true
  }
});
</script>

<style scoped>
.python-code {
  background-color: #f5f5f5;
  border-radius: 5px;
  padding: 10px;
  overflow-x: auto;
  font-family: 'Courier New', Courier, monospace;
}
</style>
</contents>