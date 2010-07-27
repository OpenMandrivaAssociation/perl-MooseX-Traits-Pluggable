%define upstream_name    MooseX-Traits-Pluggable
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An extension to MooseX::Traits
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::MOP)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(MooseX::Traits)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl-Test-use-ok
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch
Requires:  perl(MooseX::Traits)

%description
See the MooseX::Traits manpage for usage information.

Adds support for class precedence search for traits and some extra
attributes, described below.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


