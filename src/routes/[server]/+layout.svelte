<script lang="ts">
  import { resolve } from '$app/paths';

  let { children, params } = $props();
</script>

<div class="flex h-full pr-1 bg-gray-700">
  <aside class="flex flex-col w-32 bg-gray-500 space-y-2 p-2">
    <h1><a href={resolve(`/${params.server}`)}>{params.server}</a></h1>
    <nav>
      <ul>
        <!-- list of channels -->
        <li><a href={resolve(`/${params.server}/1234`)}>1234</a></li>
        <li><a href={resolve(`/${params.server}/2345`)}>2345</a></li>
        <li><a href={resolve(`/${params.server}/3456`)}>3456</a></li>
      </ul>
    </nav>
  </aside>
  <div class="flex-1 pl-3 bg-gray-700 overflow-auto custom-scrollbar">
    {@render children()}
  </div>
</div>
