# installs the package puppet_lint
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
