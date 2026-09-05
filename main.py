import asyncio
import os
import sys
import threading
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

# .envファイルを読み込み
load_dotenv()
print("hi")
# bot1、bot2、bot3、bot4をインポート
from bot1 import bot1
from bot4 import bot4


async def start_discord_bots():
    """Discord Botを起動"""
    try:
        # 環境変数からトークンを取得
        token = os.getenv('token')  # Bot1用のトークン
        
        # デバッグ: トークンの存在確認（実際の値は表示しない）
        japan_time = datetime.now(timezone(timedelta(hours=9)))
        print(f"🤖 Bot起動時刻: {japan_time}")
        print("🚀 2つのbotを同時起動中...")
        print(f"Bot1: 起動準備完了")
        print(f"Bot4: 起動準備完了")
        
        # 4つのbotを同時に起動
        await asyncio.gather(
            bot1.start(token),
            bot4.start(token)
        )
        
    except KeyboardInterrupt:
        print("\n⏹️  Bot停止中...")
        raise
    except Exception as e:
        print(f"❌ Botエラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        print("🔄 Bot クリーンアップ中...")
        # Botの終了処理
        if not bot1.is_closed():
            await bot1.close()
        if not bot4.is_closed():
            await bot4.close()

async def main():
    try:
        # 少し待ってからBotを起動
        await asyncio.sleep(1)
        
        # Discord Botを起動
        await start_discord_bots()
        
    except KeyboardInterrupt:
        print("\n⏹️  全サービス停止中...")
    except Exception as e:
        print(f"❌ メイン処理でエラーが発生しました: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("🤖 Discord Bot: 2体同時実行")
    print("⏹️  停止するには Ctrl+C を押してください")
    print("=" * 50)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        japan_time = datetime.now(timezone(timedelta(hours=9)))
        print(f"\n🕐 終了時刻: {japan_time}")
        print("✅ 正常に終了しました")
        sys.exit()
    except Exception as e:
        print(f"❌ 予期しないエラー: {e}")
        import traceback
        traceback.print_exc()
