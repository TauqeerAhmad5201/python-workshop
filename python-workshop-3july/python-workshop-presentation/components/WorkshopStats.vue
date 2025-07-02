<template>
  <div class="workshop-stats">
    <h2>Workshop Statistics</h2>
    <ul>
      <li>Total Participants: {{ totalParticipants }}</li>
      <li>Feedback Score: {{ feedbackScore }}/5</li>
      <li>Engagement Rate: {{ engagementRate }}%</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      totalParticipants: 50,
      feedbackScore: 4.8,
      engagementRate: 95
    };
  }
};
</script>

<style scoped>
.workshop-stats {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
h2 {
  color: #333;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 5px 0;
}
</style>