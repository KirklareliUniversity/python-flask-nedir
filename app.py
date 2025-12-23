from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gizli_anahtar'

yapilacaklar = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        yeni_gorev = request.form.get("gorev_adi")
        tarih = request.form.get("tarih")

        if not yeni_gorev:
            flash("Görev adı boş olamaz!", "danger")
            return redirect(url_for("index"))

        if tarih:
            bugun = date.today().strftime("%Y-%m-%d")
            if tarih < bugun:
                flash("Geçmiş bir tarih seçemezsiniz!", "danger")
                return redirect(url_for("index"))

        yapilacaklar.append({
            "gorev": yeni_gorev,
            "tamamlandi": False,
            "tarih": tarih if tarih else None
        })

        flash(f"'{yeni_gorev}' başarıyla eklendi!", "success")
        return redirect(url_for("index"))

    today = date.today().strftime("%Y-%m-%d")
    return render_template("index.html", yapilacaklar=yapilacaklar, today=today)


@app.route("/sil/<int:madde_id>")
def sil(madde_id):
    if 0 <= madde_id < len(yapilacaklar):
        silinen = yapilacaklar[madde_id]["gorev"]
        yapilacaklar.pop(madde_id)
        flash(f"'{silinen}' silindi.", "danger")

    return redirect(url_for("index"))


@app.route("/toggle/<int:madde_id>")
def toggle(madde_id):
    if 0 <= madde_id < len(yapilacaklar):
        task = yapilacaklar[madde_id]
        task["tamamlandi"] = not task["tamamlandi"]

        if task["tamamlandi"]:
            flash(f"'{task['gorev']}' tamamlandı!", "success")
        else:
            flash(f"'{task['gorev']}' yeniden aktif hale getirildi.", "warning")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
