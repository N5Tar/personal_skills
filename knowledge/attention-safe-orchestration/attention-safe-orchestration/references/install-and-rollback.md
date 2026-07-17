# Install and Roll Back

Source of record is this directory. Install only after verification and only if the
target does not exist:

~~~bash
test ! -e ~/.agents/skills/attention-safe-orchestration
cp -R knowledge/attention-safe-orchestration/attention-safe-orchestration \
  ~/.agents/skills/attention-safe-orchestration
~~~

Verify with:

~~~bash
test -f ~/.agents/skills/attention-safe-orchestration/SKILL.md
~~~

Roll back the installation without touching installed Superpowers:

~~~bash
rm -rf ~/.agents/skills/attention-safe-orchestration
~~~

To remove the experiment source, delete
`knowledge/attention-safe-orchestration/` in its Git commit/revert workflow.
