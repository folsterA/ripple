<script lang="ts">
  let { params } = $props();

  let channels = $state('');
</script>

<h1>Server: {params.server}</h1>
<h1>Channels: {channels}</h1>
<p>This is the server homepage.</p>

<!-- this would be the default home page -->
