#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-sinatra
Version  : 1.4.7
Release  : 6
URL      : https://rubygems.org/downloads/sinatra-1.4.7.gem
Source0  : https://rubygems.org/downloads/sinatra-1.4.7.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rack
BuildRequires : rubygem-rack-protection
BuildRequires : rubygem-rack-test
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-tilt

%description
# Sinatra
*æ³¨ï¼æ¬ææ¡£æ¯è±æççç¿»è¯ï¼åå®¹æ´æ°æå¯è½ä¸åæ¶ãå¦æä¸ä¸è´çå°æ¹ï¼è¯·ä»¥è±æçä¸ºåã*

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n sinatra-1.4.7
gem spec %{SOURCE0} -l --ruby > rubygem-sinatra.gemspec

%build
gem build rubygem-sinatra.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
sinatra-1.4.7.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/sinatra-1.4.7
ruby -v -I.:lib:test test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/sinatra-1.4.7.gem
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Rack/Builder/cdesc-Builder.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Rack/cdesc-Rack.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Application/cdesc-Application.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/CommonLogger/call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/CommonLogger/call_without_check-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/CommonLogger/cdesc-CommonLogger.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Ext/_const_get-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Ext/cdesc-Ext.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Ext/get_handler-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ExtendedRack/after_response-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ExtendedRack/async%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ExtendedRack/call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ExtendedRack/cdesc-ExtendedRack.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ExtendedRack/setup_close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/%3c%3c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Application/cdesc-Application.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/add_filter-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/after-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/agent-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/app-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/before-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/build-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/call-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/caller_files-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/caller_locations-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/cdesc-Base.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/cleaned_caller-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/compile%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/compile-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/condition-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/configure-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/define_singleton-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/delete-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/detect_rack_handler-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/development%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/disable-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/dispatch%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/dump_errors%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/enable-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/encoded-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/error-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/error_block%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/errors-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/escaped-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/extensions-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/filter%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/filters-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/force_encoding-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/force_encoding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/forward-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/generate_method-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/get-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/halt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/handle_exception%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/head-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/helpers-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/host_name-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/indifferent_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/indifferent_params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/inherited-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/inline_templates%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/invoke-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/invoke_hook-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/layout-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/link-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/middleware-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/mime_type-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/mime_types-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/new%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/not_found-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/options-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/pass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/patch-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/post-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/process_route-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/production%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/prototype-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/provides-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/public%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/public_dir%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/public_dir-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/put-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/quit%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/register-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/reset%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/response-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/route%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/route-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/route_eval-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/route_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/routes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/run%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/running%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/safe_ignore-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/set-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/settings-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/settings-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_common_logger-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_custom_logger-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_default_middleware-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_logging-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_middleware-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_null_logger-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_protection-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_sessions-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/setup_traps-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/start%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/start_server-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/static%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/stop%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/synchronize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/template-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/template_cache-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/templates-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/test%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/unlink-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/use-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/user_agent-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Base/warn-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Delegator/cdesc-Delegator.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/ContentTyped/cdesc-ContentTyped.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/ContentTyped/content_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/asciidoc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/builder-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/cdesc-Templates.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/coffee-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/compile_template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/creole-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/erb-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/erubis-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/find_template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/haml-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/less-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/liquid-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/markaby-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/markdown-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/mediawiki-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/nokogiri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/rabl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/radius-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/rdoc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/render-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/render_ruby-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/sass-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/scss-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/slim-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/stylus-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/textile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/wlang-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Templates/yajl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Wrapper/call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Wrapper/cdesc-Wrapper.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Wrapper/helpers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Wrapper/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Wrapper/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/Wrapper/settings-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/back-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/cache_control-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/callback-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/cdesc-Stream.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/client_error%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/closed%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/defer-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/etag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/etag_matches%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/expires-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/helpers-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/informational%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/last_modified-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/not_found%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/redirect%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/register-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/schedule-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/server_error%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/stream-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/success%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/time_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/use-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/Stream/with_params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/attachment-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/cdesc-Helpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/content_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/logger-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/mime_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/not_found-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/redirect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/send_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/session-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Helpers/url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/NotFound/cdesc-NotFound.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/%3c%3d%3e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/cdesc-AcceptEntry.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/entry-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/priority-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/respond_to%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/AcceptEntry/to_str-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/accept%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/accept-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/cdesc-Request.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/forwarded%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/idempotent%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/link%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/preferred_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/safe%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Request/unlink%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Response/body%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Response/calculate_content_length%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Response/cdesc-Response.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Response/drop_body%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Response/drop_content_info%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Response/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Response/finish-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/Response/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ShowExceptions/call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ShowExceptions/cdesc-ShowExceptions.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ShowExceptions/frame_class-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ShowExceptions/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/ShowExceptions/prefers_plain_text%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/Sinatra/cdesc-Sinatra.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-LICENSE.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_de_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_es_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_fr_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_hu_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_ja_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_ko_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_pt-br_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_pt-pt_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_ru_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/sinatra-1.4.7/ri/page-README_zh_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/AUTHORS.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.de.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.es.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.fr.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.hu.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.ja.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.ko.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.pt-br.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.pt-pt.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.ru.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/README.zh.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/examples/chat.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/examples/simple.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/examples/stream.ru
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/lib/sinatra.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/lib/sinatra/base.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/lib/sinatra/ext.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/lib/sinatra/images/404.png
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/lib/sinatra/images/500.png
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/lib/sinatra/main.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/lib/sinatra/show_exceptions.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/lib/sinatra/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/sinatra.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/asciidoctor_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/base_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/builder_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/coffee_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/compile_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/contest.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/creole_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/delegator_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/encoding_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/erb_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/extensions_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/filter_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/haml_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/helpers_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/integration/app.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/integration_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/integration_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/less_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/liquid_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/mapped_error_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/markaby_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/markdown_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/mediawiki_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/middleware_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/nokogiri_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/public/favicon.ico
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/public/hello+world.txt
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/rabl_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/rack_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/radius_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/rdoc_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/readme_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/request_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/response_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/result_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/route_added_hook_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/routing_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/sass_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/scss_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/server_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/settings_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/sinatra_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/slim_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/static_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/streaming_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/stylus_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/templates_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/textile_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/a/in_a.str
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/ascii.erb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/b/in_b.str
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/calc.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/error.builder
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/error.erb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/error.haml
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/error.sass
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/explicitly_nested.str
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/foo/hello.test
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.asciidoc
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.builder
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.coffee
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.creole
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.erb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.haml
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.less
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.liquid
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.mab
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.md
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.mediawiki
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.nokogiri
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.rabl
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.radius
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.sass
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.scss
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.slim
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.str
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.styl
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.test
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.textile
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.wlang
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/hello.yajl
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.builder
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.erb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.haml
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.liquid
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.mab
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.nokogiri
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.rabl
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.radius
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.slim
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.str
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.test
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/layout2.wlang
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/nested.str
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/views/utf8.erb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/wlang_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/sinatra-1.4.7/test/yajl_test.rb
/usr/lib64/ruby/gems/2.2.0/specifications/sinatra-1.4.7.gemspec
