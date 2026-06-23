import Link from "next/link";
import { notFound } from "next/navigation";
import { getAllAssignmentSlugs, getAssignmentDetail } from "../../lib/assignments";
import {
  statusBadgeStyles,
  statusLabels,
  typeBadgeStyles,
  typeLabels,
} from "../../components/statusStyles";

export async function generateStaticParams() {
  const slugs = await getAllAssignmentSlugs();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const detail = await getAssignmentDetail(slug);
  return { title: detail ? `${detail.title} · ICS` : "Assignment" };
}

export default async function AssignmentPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const detail = await getAssignmentDetail(slug);
  if (!detail) notFound();

  return (
    <main className="mx-auto w-full max-w-3xl px-5 py-10 sm:px-8 sm:py-14">
      {/* Back link */}
      <Link
        href="/"
        className="group inline-flex items-center gap-1.5 text-sm text-slate-400 transition-colors hover:text-slate-200"
      >
        <span aria-hidden className="transition-transform group-hover:-translate-x-0.5">
          ←
        </span>
        Back to the system
      </Link>

      {/* Header */}
      <header className="mt-6 border-b border-slate-800/80 pb-6">
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-xs font-semibold uppercase tracking-[0.18em] text-blue-400">
            Week {detail.week}
          </span>
          <span
            className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${typeBadgeStyles[detail.type]}`}
          >
            {typeLabels[detail.type]}
          </span>
          <span
            className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${statusBadgeStyles[detail.status]}`}
          >
            {statusLabels[detail.status]}
          </span>
        </div>
        <h1 className="mt-3 text-3xl font-bold tracking-tight text-white sm:text-4xl">
          {detail.title}
        </h1>
        <p className="mt-2 text-sm text-slate-400">
          Complete{" "}
          <code className="rounded bg-slate-800 px-1.5 py-0.5 font-mono text-xs text-slate-300">
            assignments/{detail.slug}/student_work.py
          </code>{" "}
          to finish this module.
        </p>
      </header>

      {/* Instructions (rendered from INSTRUCTIONS.md) */}
      {detail.contentHtml ? (
        <article
          className="assignment-prose mt-8"
          dangerouslySetInnerHTML={{ __html: detail.contentHtml }}
        />
      ) : (
        <p className="mt-8 text-sm text-slate-500">No instructions found for this assignment.</p>
      )}
    </main>
  );
}
