export default async function Home() {
  const response = await fetch("http://localhost:8000/todos");
  const data = await response.json();

  return (
    <div>
      <h1>My To-Do List</h1>
      <ul>
        {data.map((todo: any) => (
          <li key={todo.id}>{todo.object}</li>
        ))}
      </ul>
    </div>
  );
}
