# ==============================================================
# Author: Rodoflo Ferro
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-

import plotly.express as px


def plotly_figure_2d(dataframe):
    
    fig = px.scatter(
            dataframe,
            x='EDAD',
            y='SALARIO'
        )
    
    return fig


def plotly_figure_3d(dataframe):

    fig = px.scatter_3d(
            dataframe, 
            x='EDAD',
            y='SALARIO',
            z='LABEL_ENCODING',
            symbol='COMPRA',
            color='COMPRA'
        )
    
    # fig.update_traces(
    #     marker_coloraxis=None
    # )
    
    return fig