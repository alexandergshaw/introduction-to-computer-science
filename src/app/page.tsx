import { JupiterScene } from "./components/JupiterScene";
import type { SceneAssignment } from "./components/statusStyles";
import { loadAssignmentStatuses } from "./lib/assignments";

export default async function Home() {
  const statuses = await loadAssignmentStatuses();
  const completedCount = statuses.filter((status) => status.completed).length;
  const progressPercent = Math.round((completedCount / statuses.length) * 100);

  const assignments: SceneAssignment[] = statuses.map((status) => ({
    slug: status.slug,
    week: status.week,
    title: status.title,
    type: status.type,
    status: status.status,
  }));

  return (
    <JupiterScene
      assignments={assignments}
      completedCount={completedCount}
      total={statuses.length}
      progressPercent={progressPercent}
    />
  );
}
