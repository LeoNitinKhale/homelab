from django.test import TestCase

from .models import Task


class TaskTests(TestCase):
    # Task is routed to the 'ops' database — the test must opt into it.
    databases = {'ops'}

    def test_task_saves_to_ops_db(self):
        task = Task.objects.create(title='Review AAPL trade')
        self.assertEqual(task.status, Task.Status.OPEN)
        self.assertEqual(str(task), '[open] Review AAPL trade')
        self.assertIsNotNone(task.created_at)

    def test_loose_core_reference(self):
        """Cross-database link is by kind+id, not a ForeignKey."""
        task = Task.objects.create(
            title='Check peg 42', related_kind='mnemonics.peg', related_id=42,
        )
        self.assertEqual(task.related_kind, 'mnemonics.peg')
        self.assertEqual(task.related_id, 42)
