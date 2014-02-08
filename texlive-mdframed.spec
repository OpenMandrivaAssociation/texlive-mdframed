# revision 27762
# category Package
# catalog-ctan /macros/latex/contrib/mdframed
# catalog-date 2012-09-21 10:33:40 +0200
# catalog-license lppl
# catalog-version 1.6d
Name:		texlive-mdframed
Version:	1.6d
Release:	2
Summary:	Framed environments that can split at page boundaries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mdframed
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdframed.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdframed.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdframed.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package develops the facilities of framed in providing
breakable framed and coloured boxes. The user may instruct the
package to perform its operations using default LaTeX commands,
PStricks or TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mdframed/ltxmdf.cls
%{_texmfdistdir}/tex/latex/mdframed/md-frame-0.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-1.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-2.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-3.mdf
%{_texmfdistdir}/tex/latex/mdframed/mdframed.sty
%doc %{_texmfdistdir}/doc/latex/mdframed/README.txt
%doc %{_texmfdistdir}/doc/latex/mdframed/donald-duck.jpg
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-default.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-default.tex
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-pstricks.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-pstricks.tex
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-texsx.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-texsx.tex
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-tikz.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-tikz.tex
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mdframed/Makefile
%doc %{_texmfdistdir}/source/latex/mdframed/mdframed.dtx
%doc %{_texmfdistdir}/source/latex/mdframed/mdframed.ins
%doc %{_texmfdistdir}/source/latex/mdframed/mdframedmake.bat

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Oct 30 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6d-1
+ Revision: 820739
- Update to latest release.

* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6b-1
+ Revision: 812576
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 790680
- Update to latest release.

* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.4-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 783051
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3a-1
+ Revision: 772123
- Update to latest release.

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-1
+ Revision: 762667
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-3
+ Revision: 758961
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-2
+ Revision: 753843
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-1
+ Revision: 743296
- texlive-mdframed

* Tue Nov 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 732587
- texlive-mdframed

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9h-1
+ Revision: 718984
- texlive-mdframed
- texlive-mdframed
- texlive-mdframed
- texlive-mdframed

