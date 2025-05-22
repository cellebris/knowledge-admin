#
#=========================================================================================
# Knowledge Admin Utilities
#

function knowledge_admin_setup_admin () {
  namespace="$1"
  service_name="$2"
  ssh_pod="$(kubectl get pods -n "$namespace" --no-headers -o custom-columns=':metadata.name' | grep "$service_name")"

  debug "Initializing knowledge admin root user"
  debug "namespace = ${namespace}"
  debug "service_name = ${service_name}"
  debug "ssh_pod = ${ssh_pod}"

  "${__bin_dir}/kubectl" exec -n "$namespace" "$ssh_pod" -- /setup 1>>"$(logfile)" 2>&1
}

function knowledge_admin_run_command () {
  namespace="$1"
  service_name="$2"
  shift; shift;

  ssh_pod="$(kubectl get pods -n "$namespace" --no-headers -o custom-columns=':metadata.name' | grep "$service_name")"

  debug "Running management command: $@"
  debug "namespace = ${namespace}"
  debug "service_name = ${service_name}"
  debug "ssh_pod = ${ssh_pod}"

  "${__bin_dir}/kubectl" exec -it -n "$namespace" "$ssh_pod" -- /entrypoint ./manage.py "$@"
}
