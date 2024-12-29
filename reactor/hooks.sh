
function hook_build () {
  info "Installing Knowledge Manager dependencies ..."
  cd "${__knowledge_admin_project_dir}"
  npm install 1>>"$(logfile)" 2>&1
}
