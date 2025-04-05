<svelte:head>
    <title>Вход</title>
</svelte:head>

<script>
    import { toast } from "svelte-sonner";

    const uid = $props.id();
</script>

<form
    onsubmit={async (__event__) => {
        __event__.preventDefault();
        __event__.stopPropagation();
    }}
    class="p-4 mx-auto flex flex-col gap-3 w-full min-w-[250px] max-w-[360px]"
>
    <h1 class="mb-4">Вход в аккаунт</h1>
    <div class="field">
        <label for="{uid}-username">Имя пользователя</label>
        <input
            type="text"
            name="username"
            id="{uid}-username"
            autocomplete="off"
        />
    </div>
    <div class="field">
        <label for="{uid}-password">Пароль</label>
        <input
            type="password"
            name="password"
            id="{uid}-password"
            autocomplete="new-password webauthn"
        />
    </div>

    <p>Нету аккаунта? <a href="/logup">Зарегистрируйтесь</a></p>

    <button type="submit">Войти</button>
</form>
