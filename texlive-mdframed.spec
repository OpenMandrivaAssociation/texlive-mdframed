# revision 25884
# category Package
# catalog-ctan /macros/latex/contrib/mdframed
# catalog-date 2012-04-08 14:50:51 +0200
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-mdframed
Version:	1.5
Release:	1
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
