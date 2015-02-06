%define upstream_name    Perl6-Export
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Implements the Perl 6 is export trait
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Perl6-Export/
Source0:	http://www.cpan.org/modules/by-module/Perl6/Perl6-Export-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module prototypes the Perl 6 'exported' and 'exportable' traits
in Perl 5.

Instead of messing around with @EXPORT arrays, you just declare which subs
are to be exported (or are exportable on request) as part of those subs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes y | perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Perl6/
%{perl_vendorlib}/Perl6/Export.pm


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 404290
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-4mdv2009.0
+ Revision: 258221
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-3mdv2009.0
+ Revision: 246276
- rebuild

* Sun Mar 23 2008 Stefan van der Eijk <stefan@mandriva.org> 0.07-1mdv2008.1
+ Revision: 189555
- fix group
- import perl-Perl6-Export


