<script lang="ts">
  import { servers } from '$lib/stores/servers';
  import { get } from 'svelte/store';

  const all = get(servers);
  const server = all.find((s) => s.id === params.server);

  let { params } = $props();
</script>

<h1>Server: {server?.name}</h1>
<p>Description: {server?.description}</p>
<p>This is the server homepage.</p>
