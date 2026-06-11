<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import { resolve } from '$app/paths';
  import ExternalLinkHandler from '$lib/ExternalLinkHandler.svelte';
  import { invoke } from '@tauri-apps/api/core';
  import { onMount } from 'svelte';
  import type { Server } from '$lib/types';
  import '../app.css';

  let { children } = $props();

  let servers: Server[] = $state([]);

  onMount(async () => {
    servers = await invoke<Server[]>('get_servers').catch((e) => {
      console.error('get_servers failed', e);
      return [];
    });
  });
</script>

<ExternalLinkHandler />

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<div class="flex h-screen pr-1 bg-gray-700">
  <aside class="flex flex-col bg-gray-500 space-y-2 p-2">
    <nav>
      <ul>
        <li><a href={resolve('/')}>home</a></li>
        <li><a href="https://www.google.com" rel="external">external</a></li>
        {#each servers as server (server.id)}
          <li><a href={resolve('/1234')}>server: {server.name}</a></li>
        {/each}
      </ul>
    </nav>
  </aside>
  <main class="flex-1 pl-3 bg-gray-700">
    {@render children()}
  </main>
</div>
