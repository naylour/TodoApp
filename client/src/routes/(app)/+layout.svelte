<script module>
    import { NavBar } from '$lib/components';
</script>

<script>
    const { children } = $props();
</script>

{@render children()}

<NavBar />
